#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

long long MaxPairwiseProduct(const std::vector<int>& numbers) {
    long long max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                                   (long long)numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

long long MaxPairwiseProductfast(const std::vector<int>& numbers){
    int n=numbers.size();

    int maxindex1=-1;
    for(int i=0;i<n;++i){
        if((maxindex1==-1)||(numbers[i]>numbers[maxindex1]))
            maxindex1=i;
    }
    int maxindex2=-1;
    for(int i=0; i<n; ++i){
        if((i!=maxindex1)&&((maxindex2==-1)||(numbers[i]>numbers[maxindex2])))
            maxindex2=i;
    }
    return ((long long)numbers[maxindex1])*numbers[maxindex2];
}

int main() {
//    while (true){
//        int n=rand() % 100 +2;
//        std::cout<<n<<"\n";
//        std::vector<int> a;
//        for(int i=0;i<n;++i){
//            a.push_back(rand()%100000);
//
//        }
//        for(int i=0;i<n;++i){
//            std::cout<<a[i]<<' ';
//        }
//        std::cout<<"\n";
//        long long res1=MaxPairwiseProduct(a);
//        long long res2 =MaxPairwiseProductfast(a);
//        if(res1!=res2){
//            std::cout<<"wrong answer "<<res1<<' '<<res2<<"\n";
//            break;
//        } else{
//            std::cout<<"ok\n";
//        }
//
//    }

    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProductfast(numbers) << "\n";
    return 0;
}
