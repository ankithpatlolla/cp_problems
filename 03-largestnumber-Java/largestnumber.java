// # largestNumber: Write the function largestNumber(text) that takes a string of text and 
// # returns the largest int value that occurs within that text, or 0 if no such value occurs. 
// # You may assume that the only numbers in the text are non-negative integers and 
// # that numbers are always composed of consecutive digits (without commas, for example). For example:
// #     	largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
// # returns 17 (the int value 17, not the string "17"). And
// #     	largestNumber("One person ate two hot dogs!")
// # returns None (the value None, not the string "None").


class largestnumber {
	public int fun_largestnumber(String s){
		String prev = "";
		int maxi = 0;
		for(int i = 0; i < s.length(); i++) {
			String ch = Character.toString(s.charAt(i));
			try {
				int x = Integer.parseInt(ch);
				prev += s.charAt(i);
			} catch (Exception e) {
				if (Integer.parseInt(prev) > maxi) {
					maxi = Integer.parseInt(prev);
				}
				prev = "";
			}
		}
		return maxi;
	}
}
	