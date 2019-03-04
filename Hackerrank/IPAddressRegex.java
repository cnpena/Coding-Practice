/* IP Address Regex
	Class IPAddressRegex that contains a string pattern. Uses a regular expression to
	validate an IP address based on the following definition:

		IP address is a string in the form "A.B.C.D", 
			where the value of A, B, C, and D may range from 0 to 255. 
		Leading zeros are allowed. 
		The length of A, B, C, or D can't be greater than 3.
*/

class MyRegex {
    String single = "([0-9]|[0-9][0-9]|[0-1][0-9][0-9]|2[0-4][0-9]|25[0-5])";
    String pattern = single + "." + single + "." + single + "." + single;
}