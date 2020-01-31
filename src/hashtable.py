# '''
# Linked List hash table key/value pair
# '''   
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        # self.count  # current number of items in dict, nice for array, not needed for LL
        self.capacity = capacity  # (like size) Number of items in the hash table, current max length of dict
        self.storage = [None] * capacity  # 



    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        # create Linked list node if None, we are pushing Linked List kv to storage arr
        # manage logic
        '''
        
        # generate hash for index

        print("\n++++++++++++++++++")
        index = self._hash_mod(key)
        print(" index is:", index)
        print("value: ", value)
        print("hash-key: ", self._hash(key))    
        print("hash-mod: ", self._hash(key) % self.capacity)


        # verify if new LL  self.storage[0] = None, else or add to end 
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        else:
            if(self.storage[index].next == None):
                print(" Collision at index: ", index)
            orig = self.storage[index]
            self.storage[index] = LinkedPair(key,value)
            self.storage[index].next = orig 




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        doubled = HashTable(self.capacity * 2)
        # iterate into 
        for item in self.storage:
            if item is not None:
                held_item = item
                while held_item is not None:
                    doubled.insert(held_item.key, held_item.value)
                    held_item = held_item.next

        # update attrib
        self.capacity = doubled.capacity
        self.storage = doubled.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
