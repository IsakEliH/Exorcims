#include <string>

namespace log_line {
    std::string message(std::string line) {
        int index = line.find(":") + 2;

        std::string sub = line.substr(index);

        return sub;
    }

    std::string log_level(std::string line) {
        // return the log level
        int index = line.find(":") - 2;

        std::string level = line.substr(1, index);

        return level;

    }

    std::string reformat(std::string line) {
        // return the reformatted message

        return message(line) + " (" + log_level(line) + ')';

    }
}  // namespace log_line
