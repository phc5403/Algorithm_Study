# 분석 

● 내가 독해력이 딸리는건지, 문제가 의도하는바를 정확히 잡아내지 못했음.  

● **"추가된 칸이 새로운 지정 위치가 된다. 밀려난 칸이 없으면 시작 숫자와 더한다."**, **"M칸 전에 마지막 숫자에 이르면 남은 칸수는 시작 숫자부터 이어간다."**  
→ 위 2문장이 정말 이해하기 애매했다!  
→ 예제의 도식도를 보면, M칸 이동하다가 끝을 넘어가면 처음부터 다시 카운팅하게되는데, Testcase 2번을 보면 M칸 이동 후의 위치 Index가 size와 같아지는 순간이 온다.  
→ 이때, 나는 문제대로라면 남은 칸수는 시작부터 이어간다는 말에의해 index = 0 으로 돌아가는줄 알고 addtoFirst()를 했었으나 예상대로 값이 뜨질않아 그냥 Testcase 2번을 일일이 뜯어보았는데 이게 끝에 걸치면 그대로 끝에추가하는 addtoLast()가 된다는것을 알았다.  
→ 이 경우 (뒤로) 밀려난 칸이 없기 때문에 결국 **"끝에 추가된 숫자 + 처음(시작) 숫자"** 가 된다.  
→ 풀고난 지금도 개인적으로는 문장의 뜻이 모호하다고 느낌.  
