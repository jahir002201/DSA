#include <iostream>
#include <string>

// Class handling report generation
class Report {
public:
    std::string generate() const {
        // Generate report content
        return "Report Content";
    }
};

// Class handling report printing
class Printer {
public:
    void print(const std::string& report) const {
        std::cout << "Printing: " << report << std::endl;
    }
};

int main() {
    Report report;
    Printer printer;
    std::string content = report.generate();
    printer.print(content);
    return 0;
}
