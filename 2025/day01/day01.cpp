#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <string_view>
#include <chrono>
#include <charconv>

// Source: https://h-deb.ca/Sources/Mesures--Test2_0.html
template<class F, class ... Args>
auto test(F f, Args &&... args)
{
	auto pre = std::chrono::high_resolution_clock::now();
	f(std::forward<Args>(args)...);
	auto post = std::chrono::high_resolution_clock::now();
	return post - pre;
}

enum class Direction
{
	Left,
	Right
};

struct DialRotation
{
	Direction direction;
	int distance;
};

class FileCantBeOpened{};
class NotAValidNumber{};
class OutOfRangeNumber{};

class Dial
{
public:
	Dial() : password{}, current{ default_value }
	{
	}

	void readDocument(std::filesystem::path path)
	{
		std::ifstream file{ path };
		if (!file.is_open())
		{
			throw FileCantBeOpened{};
		}

		for (std::string s; std::getline(file, s);)
		{
			DialRotation dr;
			
			// Direction
			std::string_view directionString{ s.begin(), s.begin() + 1 };
			dr.direction = directionString == "L" ? Direction::Left : Direction::Right;
			
			// Distance
			auto [ptr, ec] = std::from_chars(s.data() + 1, s.data() + s.size(), dr.distance);

			if (ec == std::errc::invalid_argument)
			{
				throw NotAValidNumber{};
			}
			else if (ec == std::errc::result_out_of_range)
			{
				throw OutOfRangeNumber{};
			}
			
			// Rotate
			rotate(dr);
		}
	}

	void display() const
	{
		std::cout << "Password is : " << password << std::endl;
	}

protected:
	virtual void rotate(const DialRotation& r) noexcept = 0;

protected:
	static constexpr int default_value{ 50 };
	static constexpr int searchedValue{ 0 };
	static constexpr int numbers{ 100 };

	int password;
	int current;
};

class SimpleDial : public Dial
{
protected:
	virtual void rotate(const DialRotation& r) noexcept override
	{
		int dir = r.direction == Direction::Left ? -1 : 1;
		current += dir * r.distance;

		current %= numbers;

		if (current == 0)
		{
			password += 1;
		}
	}
};

class ComplexDial : public Dial
{
protected:
	virtual void rotate(const DialRotation& r) noexcept override
	{
		int dir = r.direction == Direction::Left ? -1 : 1;
		int previous = current;
		
		current += dir * r.distance;
		password += std::abs(current / numbers);
		
		if (previous < 0 && current >= 0 || previous > 0 && current <= 0)
		{
			password += 1;
		}
		
		current %= numbers;
	}
};

int main()
{
	SimpleDial dial1;
	auto time1 = test([&dial1] { dial1.readDocument("./input.txt"); });
	dial1.display();
	std::cout << "Time: " << std::chrono::duration_cast<std::chrono::microseconds>(time1).count() << " us." << std::endl;

	ComplexDial dial2;
	auto time2 = test([&dial2] { dial2.readDocument("./input.txt"); });
	dial2.display();
	std::cout << "Time: " << std::chrono::duration_cast<std::chrono::microseconds>(time2).count() << " us." << std::endl;
}