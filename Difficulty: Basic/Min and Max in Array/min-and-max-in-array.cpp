//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++
class Solution {
  public:
    pair<int, int> getMinMax(vector<int> arr) {
        // code here
        int max = INT_MIN;
        int min = INT_MAX;
        for(int i = 0;i < arr.size();i++){
            if (arr[i] >= max){
                max = arr[i];
            }
        }
        for(int i = 0; i < arr.size();i++){
            if (arr[i] <= min){
                min = arr[i];
            }
        }
    return {min ,max};
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        pair<int, int> pp = ob.getMinMax(arr);
        cout << pp.first << " " << pp.second << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends