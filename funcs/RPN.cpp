#include <iostream>
#include <string>
#include <stack>
#include <math.h>

void calc(std::stack <float> &arr_nums, 
          std::stack <char> &arr_ops){
    float b = arr_nums.top();    
    arr_nums.pop();
    float a = arr_nums.top();    
    arr_nums.pop();
    char nya = arr_ops.top();
    switch(nya){
        case '+':   arr_nums.push(a+b); break;
        case '-':   arr_nums.push(a-b); break;
        case '*':   arr_nums.push(a*b); break;
        case '/':   arr_nums.push(a/b); break;
    }
    arr_ops.pop();
}

void high(std::stack <float> &arr_nums, 
          std::stack <char> &arr_ops, 
          bool &counter, char symb){
    counter = false;
    if (arr_ops.empty() == false){
        char nya = arr_ops.top();
        char j = '*';
        char g = '/';
        if(nya == j ||  nya == g){
            calc(arr_nums, arr_ops);
            arr_ops.push(symb);
        }else{
        arr_ops.push(symb);
        }   
    }else{
        arr_ops.push(symb);
    }
}

void low(std::stack <float> &arr_nums, 
          std::stack <char> &arr_ops, 
          bool &counter, char symb){
    counter = false;
    if (arr_ops.empty() == false){
        char z = arr_ops.top();
        if (z == '(' || z == ')'){
            arr_ops.push(symb);
        }else{
            calc(arr_nums, arr_ops);
            arr_ops.push(symb);
        }
    }else{
        arr_ops.push(symb);
    }
}
void nums(std::stack <float> &arr_nums, 
          std::stack <char> &arr_ops, 
          bool &counter, char symb){
    float v = (float)symb - 48;
    if (counter == true){
        float x = arr_nums.top();
        arr_nums.pop();
        arr_nums.push(x * 10 + v);
    }else{
        arr_nums.push(v);
    }
}
int main(){
    std::string msg;
    std::cin >> msg;
    int n = msg.length();
    bool counter;
    std::stack<char> arr_ops;
    std::stack<float> arr_nums;
    std::string a = {'+','-','*','/','(', ')'};

    for (int i=0; i < n; i++){
        switch(msg.at(i)){
            case '*':   high(arr_nums, arr_ops, counter, msg.at(i)); break;
            case '/':   high(arr_nums, arr_ops, counter, msg.at(i)); break;
            case '+':    low(arr_nums, arr_ops, counter, msg.at(i)); break;
            case '-':    low(arr_nums, arr_ops, counter, msg.at(i)); break;
            case '(':   
                counter = false; 
                arr_ops.push(msg.at(i)); 
                break;
            case ')':
                counter = false;
                while(arr_ops.top() != '('){
                    calc(arr_nums, arr_ops);}
                arr_ops.pop();
                break;
            default:    
                nums(arr_nums, arr_ops, counter, msg.at(i));
                counter = true;
        }
    }
    while (arr_nums.size() > 1){calc(arr_nums, arr_ops);}
float res = arr_nums.top();
std::cout << floor(res*100)/100 << '\n';
}