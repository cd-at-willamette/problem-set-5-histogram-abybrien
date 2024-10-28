from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    if not data:
        return []
    value = max(data) # Determine the maximum value in the list to size the histogram array
    histogram = [0] * (value + 1)
    for num in data:
        histogram[num] += 1 # Counts the reoccurrences of each number
        pass
    return histogram

#1b
def print_histogram(hist:list[int]) -> None:
    for i in range(len(hist)):  # Loop through the index
        count = hist[i]  # Get asterisk count for index
        print(str(i) + ": " + '*' * count)  # Combining count and index
    pass 

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    gw = GWindow(width, height)
    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    pass
    number_bars = len(hist)  # Number of bars 
    bar_width = width // number_bars  # Width of each bar

    # Step to determine the maximum height for the bars
    max_count = max(hist) if max(hist) > 0 else 1  # Avoid division by zero

    # Draw each bar in the histogram
    for i in range(number_bars):  # Loop through each digit
        count = hist[i]  # Get the count for the current digit
        bar_height = (count / max_count) * height  # Scale the height based on the max count
        my_rect(i * bar_width, height - bar_height, bar_width, bar_height, 'red')  # Draw the bar
        pass


# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) 
graph_histogram(hist, 400, 400) # uncomment to test
