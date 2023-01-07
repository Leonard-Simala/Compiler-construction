/* 
 * Simple example source code
 * 
 * prints N odd numbers
 */

// (ASSIGN, #10008, 1000, )
void main() {
    /* all variables need to be declared first */
    int i;
    int j;
    int m;
    int N;
    int h;
    // (PLACEHOLDER)
    // (PLACEHOLDER)
    // (PLACEHOLDER)
    
    /* ...and then assigned to */
    i = 1;
    // (ASSIGN, #1, 1024, ) 
    // (ASSIGN, 1024, 1008, )
    // CG_PUSH_ID ... CG_PUSH_CONST ... #CG_ASSIGN ... #CG_CLOSE_STMT

    j = 1;
    // (ASSIGN, #1, 1028, )
    // (ASSIGN, 1028, 1012, )

    m = 0-1; // syntax only supports binary operations, this is how we get -1
    // (ASSIGN, #0, 1032, )
	// (ASSIGN, #1, 1036, )
	// (SUB, 1032, 1036, 5000)
	// (ASSIGN, 5000, 1016, )

    N = 15; // change me to increase number of odd numbers
    // (ASSIGN, #15, 1040, )
	// (ASSIGN, 1040, 1020, )

    if (i < N * 2 + 1) {
    // (ASSIGN, #2, 1044, )
	// (MULT, 1020, 1044, 5004)
	// (ASSIGN, #1, 1048, )
	// (ADD, 5004, 1048, 5008)
    
	// (LT, 1008, 5008, 5012)
	// (JPF, 5012, 32, )

        j = m * j;
        // (MULT, 1016, 1012, 5016)
        // (ASSIGN, 5016, 1012, )

        if (j < 0) {
        // (ASSIGN, #0, 1052, )
        // (LT, 1012, 1052, 5020)
        // (JPF, 5020, 28, )

            output(i);
            // (ASSIGN, 1008, 1004, )
            // (PRINT, 1004, , )

        } else {
        // 	(JP, 28, , )

        }
        i = i + 1;
        //	(ASSIGN, #1, 1056, )
        // (ADD, 1008, 1056, 5024)
        // (ASSIGN, 5024, 1008, )
    }
    // (JP, 14, , )
}

// instances where Var-declartion-prime would be used
// void main;
// int main [20];