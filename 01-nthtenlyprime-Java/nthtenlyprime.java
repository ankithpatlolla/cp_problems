// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


class nthtenlyprime {
	public boolean is_prime(int n) {
		if(n <= 1) {
			return false;
		}
		for (int i = 2; i < (n / 2); i++) {
			if(n % i == 0) {
				return false;
			}
		}
		return true;
	}

	public boolean is_additive(int n) {
		if (is_prime(n) == false) {
			return false;
		}
		int sum = 0;
		while (n > 0){
			sum += n % 10;
			n = n / 10;
		}
		if (is_prime(sum) == true) {
			return true;
		}
		return false;
	}
	public int fun_nthtenlyprime(int n){
		int i = 0;
		int c = -1;
		while(true) {
			if (is_additive(i) == true) {
				c++;
			}
			if (c == n) {
				break;
			}
			i++;
		}
		return i;
	}
}