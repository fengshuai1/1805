int main(i,j,k)
    
    for (i = 1; i<10; i++)
        
        for (j = 1; j<=i; j++)
            k = i*j;
            // %-5d ：-表示左对齐，5表示占五个字符长度
            printf("%d*%d*%-3d",j,i,k);
        
        printf("\n");
    return 0;
