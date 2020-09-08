class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'{self.value} -> {self.next}'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.size = 11
        self.capacity = [None] * self.size
        self.count = 0
        self.entries = []
        
    def __repr__(self):
        return str(self.capacity) 
    


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        print('self.capacity is,', len(self.capacity))
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        
        Implement this.
        """
        # keys / total number of objects the hash table can store
        return self.count / len(self.capacity)

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """                                                                                                                               
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.size

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
    
        index = self.hash_index(key)
        # store as linked list node
        node = HashTableEntry(key, value)
        
        key = self.capacity[index]
        
        self.count += 1
        
        # the key exist
        if key:
            # overwrite with the node
            self.capacity[index] = node
            self.capacity[index].next = key
        # if self.capacity[index] exist
        #   use linked list to set next to the repeated key and value
        else:
            self.capacity[index] = node
        # print('adding node', node.next)
        self.entries.append(node)
        return self.capacity[index]



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.count -= 1
        self.put(key, None)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        item = self.hash_index(key)
        
        storage = self.capacity[item]
        
        while storage:
            if storage.key == key:
                return storage.value
            storage = storage.next

    # TODO: Need Help Resizing
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # downsize
        if self.get_load_factor() < 0.2:
            new_capacity = self.size / 2
            return new_capacity
        else:
            self.size = self.size * 2
            new_capacity = [None] * self.size
            self.capacity = new_capacity
            print("sel.capacity is now ", self.capacity)
            # get key to rehash and value to correspond to key
            # for entry in self.entries:
            #     # print('key in old hashtable', entry.key, entry.value)
            #     self.put(entry.key, entry.value)
            #     # rehash all the keys in hashtable


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")
    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f'line-{i}'))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print('Resized from', old_capacity, 'to', new_capacity)


    print("")
