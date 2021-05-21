#include <iostream>
#include <string>

int main()
{
    std::cout << "Enter your name: ";

    std::string s;
    std::cin >> s;

    std::cout << "Your name is " << s << std::endl;
}