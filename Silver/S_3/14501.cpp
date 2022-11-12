#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int T;
	int P;

	int* dp = new int[N+1] {};

	for (int i = 0; i < N; i++) {
		cin >> T >> P;
		if(i + T < N+1){
			for (int j = i + T; j < N+1; j++){
				dp[j] = max(dp[j], dp[i] + P);
			}
		}
	}
	
	cout << dp[N];

	return 0;
}