import threading  # Import threading module for handling threads
import time  # Import time module to add delays
import random  # Import random module to generate random numbers

# Global variable to keep track of the number of active readers
readers_count = 0

# Locks for controlling access to shared resources
resource_lock = threading.Lock()  # Lock for resource access (writers need exclusive access)
readers_lock = threading.Lock()  # Lock for managing the readers count

# Execution time limit in seconds
execution_time_limit = 10

def reader(reader_id):
    """Function to simulate a reader thread."""
    global readers_count  # Use the global readers_count variable
    start_time = time.time()  # Record the start time

    while time.time() - start_time < execution_time_limit:  # Limit execution time
        with readers_lock:  # Acquire the readers lock to modify readers_count safely
            readers_count += 1  # Increment the count of active readers
            # If this is the first reader, lock the resource
            if readers_count == 1:
                resource_lock.acquire()  # Lock the resource for reading

        print(f"Reader {reader_id} is reading.")  # Indicate that the reader is reading
        time.sleep(random.random())  # Simulate reading time with a random sleep

        with readers_lock:  # Acquire the readers lock again for safe modification
            readers_count -= 1  # Decrement the count of active readers
            # If this is the last reader, release the resource lock
            if readers_count == 0:
                resource_lock.release()  # Unlock the resource

def writer(writer_id):
    """Function to simulate a writer thread."""
    start_time = time.time()  # Record the start time

    while time.time() - start_time < execution_time_limit:  # Limit execution time
        print(f"Writer {writer_id} is trying to write.")  # Indicate that the writer is attempting to write
        resource_lock.acquire()  # Lock the resource for exclusive writing access
        print(f"Writer {writer_id} is writing.")  # Indicate that the writer is writing
        time.sleep(random.random())  # Simulate writing time with a random sleep
        resource_lock.release()  # Unlock the resource after writing

# Create threads for readers and writers
# List comprehension to create 5 reader threads
readers = [threading.Thread(target=reader, args=(i,)) for i in range(5)]
# List comprehension to create 2 writer threads
writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

# Start all reader threads
for r in readers:
    r.start()
# Start all writer threads
for w in writers:
    w.start()

# Wait for all reader threads to finish
for r in readers:
    r.join()
# Wait for all writer threads to finish
for w in writers:
    w.join()
