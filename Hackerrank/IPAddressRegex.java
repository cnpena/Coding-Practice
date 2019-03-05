/* IP Address Regex
	Class IPAddressRegex uses a regular expression to
	validate an IP address based on the following definition:

		IP address is a string in the form "A.B.C.D", 
			where the value of A, B, C, and D may range from 0 to 255. 
		Leading zeros are allowed. 
		The length of A, B, C, or D can't be greater than 3.
*/

/* To match the regular expression to valid IP addresses, must consider
	values of length 1, 2, and 3.
		For values of length 1, can be any digit 0-9
		For values of length 2, each can be any digit 0-9
		For values of length 3, can be
			000-199 OR
			200-249 OR
			250-255
*/
			
class IPAddressRegex {
	String oneDigit = "[0-9]";
    String twoDigits = "[0-9][0-9]";
    String threeDigits = "[0-1][0-9][0-9]|[2][0-4][0-9]|25[0-5]";
    String exp = "(" + oneDigit + "|" + twoDigits + "|" + threeDigits + ")";
    String pattern = exp + "." + exp + "." + exp + "." + exp;
}