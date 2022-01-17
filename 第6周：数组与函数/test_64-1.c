
//如何用一个两重循环实现行和列的检查
//视频中所说的用一个两重循环实现行和列的检查该怎么做？


//将行检查、列检查、斜检查合并在一起：

#include<stdio.h>



int juice(int SIZE,int numOfX,int numOfO);//函数原型声明 

int main(){//这个代码只判定棋盘上的情况是谁赢，不算完整游戏代码 
	
	const int SIZE=3;
	
	int board[SIZE][SIZE];
	
	int i,j;
	
	int numOfX;//X的个数 
	
	int numOfO; //O的个数
	
	int numOfX_r,numOfX_c,numOfO_r,numOfO_c;
	
	int numOfX_Left,numOfO_Left,numOfX_Right,numOfO_Right;
	
	int result=-1;//-1:没人赢	1：X方赢	0：O方赢
	
	
	
	//读入矩阵
	
	for(i=0;i<SIZE;i++){
		
		for(j=0;j<SIZE;j++){
			
			scanf("%d",&board[i][j]);
			
		}
		
	} //测试用例：0 0 1 0 1 1 1 -1 0：正确结果:X方赢 
	
	//1 0 1 0 1 1 1 0 0：X赢 
	
	
	
	//检查行、检查列合并 ：检查board[0][1]的同时，检查 board[1][0] 
	
	numOfX_Left = numOfO_Left = 0;//左斜线 
	
	numOfX_Right = numOfO_Right = 0;//右斜线 //这两不能放在i的循环内，否则，每到新一行，它被清理一次 
	
	for(i=0;i<SIZE&&result==-1;i++){
		
		numOfX_r=0;//横向上X的个数 row
		
		numOfO_r=0;//横向上O的个数 
		
		numOfX_c=0;//纵向上X的个数 culomn
		
		numOfO_c=0;//纵向上O的个数
		
		for(j=0;j<SIZE;j++){
			
			//行 
			
			if(board[i][j]==1){//棋盘上，1表示X，0表示O ,-1表示还没棋子 
				
				numOfX_r++;
				
			}else if(board[i][j]==0){
				
				numOfO_r++; 
				
			}
			
			//列 
			
			if(board[j][i]==1){
				
				numOfX_c++;
				
			} else if(board[j][i]==0){
				
				numOfO_c++; 
				
			} 
			
			//左斜线 
			
			if(i==j&&board[i][j]==1){
				
				numOfX_Left++;
				
			} else if(i==j&&board[i][j]==0){
				
				numOfO_Left++;
				
			}
			
			//右斜线
			
			if(j==SIZE-i-1&&board[i][j]==1){
				
				numOfX_Right++;
				
			} else if(j==SIZE-i-1&&board[i][j]==0){
				
				numOfO_Right++;
				
			} 
			
		}
		
		result=juice(SIZE,numOfX_r,numOfO_r);
		
		if(result!=-1){
			
			break; 
			
		} 
		
		result=juice(SIZE,numOfX_c,numOfO_c);
		
		if(result!=-1){
			
			break; 
			
		} 
		
		result=juice(SIZE,numOfX_Left,numOfO_Left);
		
		if(result!=-1){
			
			break; 
			
		} 
		
		result=juice(SIZE,numOfX_Right,numOfO_Right);
		
		if(result!=-1){
			
			break; 
			
		} 
		
	} 
	
	
	
	switch(result){
		
	case 0:
		
		printf("O方赢了\n");
		
		break; 
		
	case 1:
		
		printf("X方赢了\n");
		
		break;
		
	case -1:
		
		printf("还没人赢，游戏继续\n"); 
		
		break;
		
	}
	
	
	
	return 0;
	
} 



//判断是谁赢了 

int juice(int SIZE,int numOfX,int numOfO){
	
	int result; 
	
	if(numOfX==SIZE){
		
		result=1;//X方赢了 
		
	} else if(numOfO==SIZE){
		
		result=0;//O方赢了 
		
	} else{
		
		result=-1;//没人赢 
		
	} 
	
	return result;
	
}


