/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
	var i = 0, j = 0;
	var nLive = 0;
	var nAliveCnt = 0;

	var matrixRow = board.length;
	var matrixColumn = board[0].length;

	var copyMatrix = new Array();

	for (i = 0; i < matrixRow; i++) 
	{
		copyMatrix[i] = new Array();

		for (j = 0; j < matrixColumn; j++)
		{
			if (board[i][j] == 1) 
			{
				nLive = nLive + 1;
			}
			copyMatrix[i][j] = board[i][j];
		}
	}

	for(i = 0; i < matrixRow; i++)
	{
		for(j = 0; j < matrixColumn; j++)
		{
			nAliveCnt = 0;

			if ((i-1 >= 0) && (j - 1 >=0) && (board[i-1][j-1] == 1))
			{
				nAliveCnt++;
			}

			if((i-1 >= 0) && (board[i-1][j] == 1))
			{
				nAliveCnt++;
			}

			if((i - 1 >= 0) && ( j + 1 < matrixColumn) && (board[i-1][j+1] == 1))
			{
				nAliveCnt++;
			}

			if(( j - 1 >= 0) && (board[i][j -1] == 1))
			{
				nAliveCnt++;
			}

			if(( j + 1 < matrixColumn) && (board[i][j+1] == 1))
			{
				nAliveCnt++;
			}

			if(( i + 1 < matrixRow) && ( j - 1 >=0) && (board[i+1][j-1] ==1))
			{
				nAliveCnt++;
			}

			if(( i + 1 < matrixRow) && (board[i+1][j] == 1))
			{
				nAliveCnt++;
			}

			if(( i + 1 < matrixRow) && ( j + 1 <matrixColumn) && (board[i+1][j+1] == 1))
			{
				nAliveCnt++;
			}

			if (board[i][j] == 1)
			{
				if ((nAliveCnt == 2) || (nAliveCnt == 3))
				{
					copyMatrix[i][j] = 1;
				}
				else
				{
					copyMatrix[i][j] = 0;
					nLive--;
				}
			}

			if(board[i][j] == 0)
			{
				if (nAliveCnt == 3)
				{
					copyMatrix[i][j] = 1;
					nLive++;
				}
			}
		}
	}

	for(i = 0; i < matrixRow; i++)
	{
		for (j =0; j <matrixColumn; j++)
		{
			board[i][j] = copyMatrix[i][j];
		}
	}

};