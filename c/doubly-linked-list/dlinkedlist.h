struct dlnode {
  int val;
  struct dlnode *next;
  struct dlnode *prev;
};

void initialize(void);
int size(void);
int empty(void);
void push_front(int);
void push_back(int);
int front(void);
int back(void);
int value_at(int);
void erase(int);
int remove_value(int);
int value_n_from_end(int);
int pop_front(void);
int pop_back(void);
void insert(int, int);
void reverse(void);