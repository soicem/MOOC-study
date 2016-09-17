-participation : 3명(김기한, 김남규, 김선용)
-info

-study 요약

1. 복잡도

void function(int n){
   int i, j, k, count = 0;
   for(i=n/2; i<=n; i++)
      for(j=1; j+n/2<=n; j=j++)
         for(k=1; k<=n; k=k*2)
            count++;
}

위 코드의 복잡도는 얼마인가요?
답 : n * n * log n
