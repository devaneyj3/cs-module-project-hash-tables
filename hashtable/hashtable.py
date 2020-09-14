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
        self.capacity = MIN_CAPACITY
        self.table = [None] * self.capacity
        self.count = 0

        
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
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        
        Implement this.
        """
        # keys / total number of objects the hash table can store
        return self.count / len(self.table)

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
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        # store as linked list node
        node = HashTableEntry(key, value)
        # print(node)
        key = self.table[index]
        
        self.count += 1
        
        # the key exist
        if key:
            # overwrite with the node
            self.table[index] = node
            self.table[index].next = key
        # if self.capacity[index] exist
        #   use linked list to set next to the repeated key and value
        else:
            self.table[index] = node
        # print('adding node', node.next)
        print(self.table)
        return self.table[index]



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
        
        storage = self.table[item]
        
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
        self.capacity = new_capacity
        # downsize
        if self.get_load_factor() < 0.2:
            new_capacity //= 2
            self.capacity = new_capacity
            old_table = self.table
            self.table = [None]*self.capacity
            #Traverse the old table and pass each previous val into the put method of our new empty table
            for node in old_table:
                while True:
                    if node != None:
                        self.put(node.key, node.value)
                        if node.next == None:
                            break
                        node = node.next
                    else: break
        if self.get_load_factor() > 0.7:
            # new_capacity *= 2
            self.capacity = new_capacity
            # get key to rehash and value to correspond to key
            old_table = self.table
            self.table = [None] * self.capacity
            for node in old_table:
                while True:
                    if node != None:
                        self.put(node.key, node.value)
                        if node.next == None:
                            break
                        node = node.next
                    else: break


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
    ht.put("key-10", "val-10")
    ht.put("key-11", "val-11")
    ht.put("key-12", "val-12")
    # print(ht.get("key-12"))
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f'line-{i}'))
        
    print(ht)

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print('Resized from', old_capacity, 'to', new_capacity)


    # print("")
