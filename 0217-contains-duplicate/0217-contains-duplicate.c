#include <stdbool.h>
#include <stdlib.h>

typedef struct HashNode {
    int key;
    struct HashNode* next;
} HashNode;

#define HASH_SIZE 100003

int hash(int key) {
    if (key < 0) key = -key;
    return key % HASH_SIZE;
}

bool insertAndCheck(HashNode** hashTable, int key) {
    int index = hash(key);
    HashNode* current = hashTable[index];

    while (current) {
        if (current->key == key) return true;
        current = current->next;
    }

    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->next = hashTable[index];
    hashTable[index] = newNode;

    return false;
}

bool containsDuplicate(int* nums, int numsSize) {
    HashNode* hashTable[HASH_SIZE] = { NULL };

    for (int i = 0; i < numsSize; i++) {
        if (insertAndCheck(hashTable, nums[i])) {
            return true;
        }
    }

    for (int i = 0; i < HASH_SIZE; i++) {
        HashNode* current = hashTable[i];
        while (current) {
            HashNode* temp = current;
            current = current->next;
            free(temp);
        }
    }

    return false;
}
