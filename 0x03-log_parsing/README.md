# Log Parsing

## Task Overview

In this task, you are required to write a Python script that reads lines from standard input (stdin) and processes log entries in a specific format. The script should:

- **Compute the total file size** after reading each line.
- **Track the number of occurrences** of various HTTP status codes (such as 200, 301, 400, 401, 403, 404, 405, and 500).
- **Print statistics** after every 10 lines and when interrupted by a keyboard signal (`CTRL + C`).

### Input Format:
Each log entry follows this format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Where:
- `<IP Address>` is the IP address of the client (e.g., `12.34.56.78`).
- `[<date>]` is the timestamp in square brackets (e.g., `[2023-10-25 15:00:00]`).
- `"GET /projects/260 HTTP/1.1"` is the HTTP request (for this task, the request is constant).
- `<status code>` is a valid HTTP status code (e.g., `200`).
- `<file size>` is the size of the file sent in response (e.g., `1024`).

### Output:
After every 10 lines and on `CTRL + C`, print the following:
1. **Total file size**: The sum of all the `<file size>` values encountered so far.
2. **Number of lines by status code**: The count of valid status codes seen so far, in ascending order. Do not print any status code that has not been encountered.

### Example:
After reading 10 lines or pressing `CTRL + C`, the output should look like this:

File size: 5213 200: 2 401: 1 403: 2 404: 1 405: 1 500: 3

---

## Requirements

- **Language**: Python 3.x
- The script should read from `stdin` line by line.
- If a line does not match the specified format, it should be skipped.
- After every 10 lines, the current statistics (total file size and status code counts) should be printed.
- If a keyboard interruption (`CTRL + C`) occurs, the statistics should be printed before exiting.

---

## Functionality Breakdown

1. **Processing the input**:
   - Each line represents a log entry, and you should extract the IP address, date, status code, and file size.
   - The script should only count lines that follow the correct format.

2. **Tracking the statistics**:
   - Use a variable to keep a running total of the file sizes.
   - Use a dictionary or similar structure to track the number of occurrences of each HTTP status code.

3. **Printing the output**:
   - After every 10 lines or when interrupted, print:
     - The total file size (`File size: <total size>`).
     - The status codes in ascending order along with their counts (`<status code>: <count>`).
   - Skip any status codes that were not encountered.

---

## Example of Script Execution

You can generate sample logs using the `0-generator.py` script and feed them into your script. Here’s how it would work:

```bash
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

---

### Edge Cases

1. Invalid input format: If the line doesn't match the expected format, it should be skipped.


2. Incomplete or missing fields: If status codes or file sizes are missing or not in integer form, they should be ignored.


3. No valid status codes: If no valid status codes are encountered, the script should only print the total file size.




---

### How to Run

1. Clone the repository:
```bash
git clone https://github.com/your_username/alx-interview.git
```

2. Navigate to the log parsing directory:
```bash
cd 0x03-log_parsing
```

3. To run the script with a sample generator:
```bash
./0-generator.py | ./0-stats.py
```

4. Alternatively, you can manually input log entries and see the statistics:
```
cat access_log.txt | ./0-stats.py
```



---

### Testing

Create or use an existing file with log entries in the correct format. You can test your script by feeding the logs via stdin and checking the output at every 10 lines or on CTRL + C.

Example:
```bash
cat sample_log.txt | ./0-stats.py
```

---

Author

Precious A.

GitHub: Nadira3


---

### Summary of Sections:
1. **Task Overview**: Explains the purpose of the task and details the input/output format.
2. **Requirements**: Lists the requirements for running the script.
3. **Functionality Breakdown**: Provides a step-by-step explanation of the logic behind the task.
4. **Example of Script Execution**: Illustrates how the script behaves with sample inputs.
5. **Edge Cases**: Lists scenarios to account for in the script.
6. **How to Run**: Instructions on running the script in different environments.
7. **Testing**: How to test the solution with different inputs.
8. **Author**: A placeholder for your personal information.
