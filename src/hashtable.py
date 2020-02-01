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
        # good prime number
        salt = 5381

        # letter scramble
        for char in key:
            hash_val = ((salt << 5) + salt) + ord(char)

        return hash_val


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        print("\n ******* ")
        # return self._hash(key) % self.capacity

        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        # create Linked list node if None, we are pushing Linked List kv to storage arr
        # manage logic
        '''
        
        # generate hash for index

        # print("\n++++++++++++++++++")
        index = self._hash_mod(key)
        print("index is:", index)
        print("value: ", value)
        print("hash-key: ", self._hash(key))    
        print("hash-mod: ", self._hash(key) % self.capacity)


        # verify if new LL  self.storage[0] = None, else or add to head!!
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        else:
            if(self.storage[index].next == None):
                print("!!!!!!  Collision at index: ", index)
            old_head = self.storage[index]

            self.storage[index] = LinkedPair(key,value) # set up new node
            self.storage[index].next = old_head #
            print("current head value: %s: " % ( self.storage[index].value ) )

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        ll_node = 0

        if self.storage[index] is None:
            return "Key does not exist in Hash Table, nothing to remove"
        else:
            if self.storage[index].key == key:
                print("this key was removed at head location",  key)
                self.storage[index].value = None
            else:    
                current = self.storage[index].next # get next node location
                while current is not None:
                    ll_node += 1
                    if current.key == key:
                        current.value = None
                        return ("removed node with key: %s at ll node: %i" % (current.key, ll_node))
                    current = current.next     

                if current is None:
                    return "Key does not exist in Hash Table, nothing to remove"    

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        ll_node = 0

        if self.storage[index] is None:
            return None

        # loop through hash table & chain for key
        else:
            if self.storage[index].key == key:
                print("key %s found at hash table index %i : " % (key, index))
                return self.storage[index].value

            else:   # iterate through ll chain
                current = self.storage[index].next
                while current is not None:    
                    ll_node += 1
                    if current.key == key:
                        print("hash table index: ", index)
                        print("ll node location is: ", ll_node)
                        #  print(">>>>>  this is it: " , current.value)
                        return current.value
                    else:
                        current = current.next    
                if current is None:
                    return None
        # 


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
    ht.insert("line_4", ">> gonna remove this one !!")

    print("")

    # # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))

    print(ht.remove("Does not exist"))
    print(ht.remove("line_4"))
    # print(ht.remove("line_3"))
    # print(ht.remove("line_1"))

    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print(ht.retrieve("line_4"))

    print(ht.retrieve("Does not exist"))
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
