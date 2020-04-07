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
        self.count = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


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

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        if self.count >= (self.capacity * .7):
            self.resize()     
        ll_temp = LinkedPair(key, value)
        # check if mod is full
        key_location = self._hash_mod(key)
        # if full add to next
        if self.storage[key_location]:
            # find if next exists
            if self.storage[key_location].next:
                # if next exists iterate to find the final node
                temp_next = self.storage[key_location]
                # check first value in the bucket
                if temp_next.key == key:
                    self.storage[key_location].value = value
                # iterate
                while temp_next.next:
                    temp_next = temp_next.next
                    if temp_next.key == key:
                        temp_next.value = value
                    elif temp_next.next == None:
                        temp_next.next = ll_temp
                        self.count += 1
            # if next is None (only one value in the mod) add to it
            else:
                if self.storage[key_location].key == key:
                    self.storage[key_location].value = value
                else:
                    self.storage[key_location].next = ll_temp
                    self.count += 1
        else:
            # add the key and value to that location
            self.storage[key_location] = ll_temp
            self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # get location of key
        key_location = self._hash_mod(key)
        # check if there is more than one value in location
        if self.storage[key_location] and self.storage[key_location].next:
            # if there is more than one check keys
            temp_next = self.storage[key_location]
            temp_prev = temp_next
            # test the first value
            if self.storage[key_location].key == key:
                self.storage[key_location] = temp_next.next

            while temp_next.next:
                temp_next = temp_next.next
                if temp_next.key == key:
                    temp_prev.next = temp_next.next
                    self.count -= 1
                else:
                    temp_prev = temp_next
                    
        # check to see if location is populated
        if self.storage[key_location]:
            # remove the LL pair
            self.storage[key_location] = None
            self.count -= 1
        # else print warning
        else:
            return -1


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get key location
        key_location = self._hash_mod(key)
        # see if there is more than one value in the mod location
        if self.storage[key_location] and self.storage[key_location].next:
            # if there is more than one, check keys
            temp_next = self.storage[key_location]
            if self.storage[key_location].key == key:
                return self.storage[key_location].value
            # iterate
            while temp_next.next:
                temp_next = temp_next.next
                # if we find the key
                if temp_next.key == key:
                    # return the value
                    return temp_next.value
            # once we finish iterating and nothing has been returned
            # value does not exist, return none
            return None

        # check if location is populated
        if self.storage[key_location]:
            return self.storage[key_location].value
            
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double capacity
        self.capacity *= 2
        # making temp hashtable to allow the use of our insert function
        temp_storage = HashTable(self.capacity)
        # iterate through values in storage
        for i in self.storage:
            if i:
                # if there is a next, iterate through those
                if i.next:
                    # setting iterate value
                    temp_next = i
                    # working through first value to avoid missing last value with while loop
                    temp_storage.insert(i.key, i.value)
                    # the while loop to iterate
                    while temp_next.next:
                        # changing to allow the last value to be iterated
                        temp_next = temp_next.next
                        # adding to temp_storage
                        temp_storage.insert(temp_next.key, temp_next.value)
                # if just one value
                else:
                    # add to temp storage
                    temp_storage.insert(i.key, i.value)
        # changing our current storage to temp storage
        self.storage = temp_storage.storage
        # removing the temp object just in case
        temp_storage = None


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")

# ht = HashTable(8)

# print(ht.capacity)
# ht.insert("key-0", "val-0")
# print(ht.capacity)
# ht.insert("key-1", "val-1")
# print(ht.capacity)
# ht.insert("key-2", "val-2")
# print(ht.capacity)
# ht.insert("key-3", "val-3")
# print(ht.capacity)
# ht.insert("key-4", "val-4")
# print(ht.capacity)
# ht.insert("key-5", "val-5")
# print(ht.capacity)
# ht.insert("key-6", "val-6")
# print(ht.capacity)
# ht.insert("key-7", "val-7")
# print(ht.capacity)
# ht.insert("key-8", "val-8")
# print(ht.capacity)
# ht.insert("key-9", "val-9")
# print(ht.capacity)


# return_value = ht.retrieve("key-0")
# print(return_value)
# return_value = ht.retrieve("key-1")
# print(return_value)
# return_value = ht.retrieve("key-2")
# print(return_value)
# return_value = ht.retrieve("key-3")
# print(return_value)
# return_value = ht.retrieve("key-4")
# print(return_value)
# return_value = ht.retrieve("key-5")
# print(return_value)
# return_value = ht.retrieve("key-6")
# print(return_value)
# return_value = ht.retrieve("key-7")
# print(return_value)
# return_value = ht.retrieve("key-8")
# print(return_value)
# return_value = ht.retrieve("key-9")
# print(return_value)

