#include <iostream>
using namespace std;

int gcd(int a, int b)
{
	int c;
	while (b != 0)
	{
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int lcm(int a, int b)
{
	return a * b / gcd(a, b);
}

int main() {

	string s1;
	string s2;

	cin >> s1;
	cin >> s2;

	string ans1 = "";
	string ans2 = "";

	int lcm_ = lcm(s1.size(), s2.size());

	for (int i = 0; i < (lcm_ / s1.size()); i++) {
		ans1 += s1;
	}

	for (int i = 0; i < (lcm_ / s2.size()); i++) {
		ans2 += s2;
	}

	if (ans1.compare(ans2) == 0) {
		cout << 1 << endl;
	}
	else {
		cout << 0 << endl;
	}

	return 0;
}