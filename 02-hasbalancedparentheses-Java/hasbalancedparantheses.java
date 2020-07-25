// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.

import java.util.*;

class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s){
		s = s.trim();
		Stack st = new Stack();
		for (int k = 0; k < s.length(); k++) {
			char i = s.charAt(k);
			if (i != '(' || i != ')') {
				continue;
			}
			else if (i == '(') {
				st.push(i);
			} else if((char)(st.pop()) != '(') {
				return false;
			}
		}
		if (st.isEmpty()) {
			return true;
		}
		return false;	
	}
}
	