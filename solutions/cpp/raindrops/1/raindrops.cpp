#include "raindrops.h"
#include <iostream>
#include <string>

namespace raindrops {


	std::string convert(int number) {

		// Divisible by 3
		std::string pling = "Pling";

		// Divisible by 5
		std::string plang = "Plang";

		// Divisible by 7
		std::string plong = "Plong";

		std::string final_string;

		if (number % 3 == 0) {
			final_string.append(pling);
		}
		if (number % 5 == 0) {
			final_string.append(plang);
		}
		if (number % 7 == 0) {
			final_string.append(plong);
		}
		if (final_string.length() == 0) {
			final_string.append(std::to_string(number));
		};
		return final_string;
	};

}  // namespace raindrops