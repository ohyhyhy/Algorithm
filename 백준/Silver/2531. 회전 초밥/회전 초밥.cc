#include <iostream>
#include <set>
using namespace std;
void init(int *s) {
	for (int i = 0; i < 3001; i++) {
		s[i] = 0;
	}
}

int dup(int s[], int d) { //초밥종류의 개수
	int res = 0;
	for (int i = 0; i <= d; i++) {
		if (s[i] >= 1) {
			res += 1;
		}
	}

	return res;
}

int main() {
	int N, n, d, k, c, j = 0;
	int A[33000];
	int s[3001] = { 0 };

	cin >> N >> d >> k >> c;
	//A = (int*)malloc(sizeof(int) * N + k - 1);
	//A배열에 원소가 들어있는 개수는 N+k-1
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	int idx = 0, idx2 = 0, cnt = 0;
	int head = 0, end = k,  ans = -1, b = 0;

	// 범위 (0-k) (1-k+1)

	while (head < N) 
	{
		int i = head;
		while (i < end) 
		{
			s[A[i % N]]++;
			i = (i + 1);
		}

		//idx = ++head;
		int temp = dup(s, d);
		int ans2 = temp;

		if (s[c] == 0) { //배열에 c가 없는 경우
			ans2 += 1;
		}

		ans = max(ans2, ans);

		head++;
		end++;
		init(s);
	} 

	cout << ans;
}

