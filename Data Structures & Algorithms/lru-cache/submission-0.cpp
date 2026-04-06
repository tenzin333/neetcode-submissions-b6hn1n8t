class Node {
public:
    int key;
    int value;
    Node* previous;
    Node* next;
    Node(int k,int v) : key(k),value(v),previous(nullptr),next(nullptr){}
};

class LRUCache {
private:
    int cap;
    unordered_map<int,Node*> cache;
    Node* left;
    Node* right;

    void remove(Node* node){
        Node* prev = node->previous;
        Node* nxt = node->next;
        prev->next = nxt;
        nxt->previous=prev;
    }

    void insert(Node* node){
            Node* prev = right->previous;
            prev->next = node;
            node->previous = prev;
            node->next = right;
            right->previous = node;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
        cache.clear();
        left = new Node(0,0);
        right = new Node(0,0);
        left->next = right;
        right->previous = left;
    }
    
    int get(int key) {
        if(cache.find(key)!=cache.end()){
            Node* node = cache[key];
            remove(node);
            insert(node);
            return node->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(cache.find(key)!=cache.end()){
            remove(cache[key]);
        }
        Node* newNode = new Node(key,value);
        cache[key] = newNode;
        insert(newNode);
        if(cache.size()>cap){
            Node* lru = left->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }

    }
};
