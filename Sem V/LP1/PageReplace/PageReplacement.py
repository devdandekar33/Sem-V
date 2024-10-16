class PRalgo:
    def __init__(self, page_numbers, max_num_frames) -> None:
        # Initialize the page numbers and maximum number of frames
        self.page_numbers = page_numbers
        self.max_num_frames = max_num_frames

    def FIFO(self):
        frames = []  # List to hold currently loaded frames
        miss_count = 0  # Count of page misses

        # Iterate through the given page numbers
        for i in range(len(self.page_numbers)):
            # Check if the current page is not in the frames
            if self.page_numbers[i] not in frames:
                miss_count += 1  # Increment miss count
                # If frames are full, remove the oldest frame
                if len(frames) == self.max_num_frames:
                    frames.pop(0)  # Deleting the oldest element
                # Add the new page to the frames
                frames.append(self.page_numbers[i])
                print(str(self.page_numbers[i]).ljust(5) + "Miss".ljust(5) + str(frames))
            else:
                print(str(self.page_numbers[i]).ljust(5) + "Hit".ljust(5) + str(frames))

        return miss_count, len(self.page_numbers) - miss_count  # Return miss and hit counts

    def optimal_approach(self):
        frames = []  # List to hold currently loaded frames
        miss_count = 0  # Count of page misses

        # Iterate through the given page numbers
        for i in range(len(self.page_numbers)):
            # Check if the current page is not in the frames
            if self.page_numbers[i] not in frames:
                miss_count += 1  # Increment miss count
                # If frames are full, replace the page that won't be used for the longest time
                if len(frames) == self.max_num_frames:
                    farthest_index = max(
                        (index for index, page in enumerate(frames) if page not in self.page_numbers[i:])
                    )
                    frames[farthest_index] = self.page_numbers[i]  # Replace the page
                else:
                    frames.append(self.page_numbers[i])  # Add the new page
                print(str(self.page_numbers[i]).ljust(5) + "Miss".ljust(5) + str(frames))
            else:
                print(str(self.page_numbers[i]).ljust(5) + "Hit".ljust(5) + str(frames))

        return miss_count, len(self.page_numbers) - miss_count  # Return miss and hit counts

    def least_recently_used(self):
        frames = []  # List to hold currently loaded frames
        frame_ages = []  # List to track how long pages have been in frames
        miss_count = 0  # Count of page misses

        # Iterate through the given page numbers
        for i in range(len(self.page_numbers)):
            # Increment age of each page in the frames
            for j in range(len(frame_ages)):
                frame_ages[j] += 1  # Increase age of all frames

            # Check if the current page is not in the frames
            if self.page_numbers[i] not in frames:
                miss_count += 1  # Increment miss count
                # If frames are full, replace the least recently used page
                if len(frames) == self.max_num_frames:
                    max_index = frame_ages.index(max(frame_ages))  # Find the index of the oldest page
                    frame_ages.pop(max_index)  # Remove the age of that page
                    frames.pop(max_index)  # Remove the page itself
                    frames.insert(max_index, self.page_numbers[i])  # Insert the new page
                    frame_ages.insert(max_index, 0)  # Reset the age for the new page
                else:
                    frames.append(self.page_numbers[i])  # Add the new page
                    frame_ages.append(0)  # Initialize the age for the new page
                print(str(self.page_numbers[i]).ljust(5) + "Miss".ljust(5) + str(frames))
            else:
                # Page hit, reset its age to zero
                index = frames.index(self.page_numbers[i])
                frame_ages[index] = 0  # Reset the age of the page
                print(str(self.page_numbers[i]).ljust(5) + "Hit".ljust(5) + str(frames))
        return miss_count, len(self.page_numbers) - miss_count  # Return miss and hit counts


# Input the number of frames
n = int(input("Enter number of pages : "))
pages = []
for i in range(n):
    ele = int(input(f"Enter page number {i + 1}: "))
    pages.append(ele)

# Input the maximum number of frames
m = int(input("Enter the maximum number of frames: "))

# Create an instance of PRalgo
algo = PRalgo(pages, m)

# Provide user with a choice of algorithm to execute
print("\nChoose the algorithm to execute:")
print("1. First In First Out (FIFO)")
print("2. Optimal Page Replacement")
print("3. Least Recently Used (LRU)")
choice = int(input("Enter your choice (1/2/3): "))

# Execute the selected algorithm and print results
if choice == 1:
    print("\nExecuting First In First Out (FIFO)...")
    miss_count, hit_count = algo.FIFO()
elif choice == 2:
    print("\nExecuting Optimal Page Replacement...")
    miss_count, hit_count = algo.optimal_approach()
elif choice == 3:
    print("\nExecuting Least Recently Used (LRU)...")
    miss_count, hit_count = algo.least_recently_used()
else:
    print("Invalid choice! Please enter 1, 2, or 3.")

# Print the hit and miss counts
if choice in [1, 2, 3]:
    print(f"Hit count: {hit_count} Miss count: {miss_count}")

# Sample page reference string
# frames = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
#m=4
