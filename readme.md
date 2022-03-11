Hi!

If you just found this repository while browsing github, there's nothing to see here really.
However, if you have been given link to this repository, it means that you are participating in the recruitment process for Contractbook.
It also means that congratulations are in order - you already passed the first interview and made it into a second stage.
So: Congratulations! :tada:

Now, let's get down to business.

You have been invited to a slack channel. There you should have received a link to swagger page of running application.
## Story
You have been asked to join a small team of developers who have lost their QA person about 6 months ago. As a subject matter expert, you are asked to help them improve quality - it is up to you to suggest changes.

This is the back-end side of a larger project (front-end is out of scope for this task)

Using GUI, end users will load buffer with data and then pass the pattern to be searched for.

## Requirements
The goal of the application they are working on is to check if a specific pattern appears in a long list of numbers. For example given a pattern `5 12 54` and numbers `1 56 12 4 23 5 12 54 32 2 65 23` we should return true.

Data is loaded to a buffer with requests to `/load` REST API endpoint in chunks. A call to a separate API endpoint `/check` checks if the pattern is present in the buffer and clears the buffer at the same time (buffer is cleared only after successful `/check` request). There is no separate GUI for this feature (this module will be added in the main app in configuration). Buffer is filled in by sending numbers in chunks (multiple `/load` requests). Chunk should be no larger than 200 elements. Pattern is sent in one request and has the same 200 elements limit as a chunk. `/check` endpoint returns status code 200 with an exists field set to either true or false. It returns true if the pattern appears at least once in numbers. If pattern is sent empty there is no match so the expected result is false. If buffer is empty when `/check` is called it should return a `400` error code. When more than 200 elements are sent `413` error code should be returned. Both pattern and numbers are arrays of int (all integers allowed, both positive and negative). Both pattern and numbers allow a `null` to appear in them. On production data will be supplied by external users, if it contains any other value than an integer or a `null` a `400` error code should be returned. If a `null` is passed as part of a pattern it matches any number (sort of a wildcard). If a `null` is passed as part of numbers it indicates missing data and it should not match anything else than a `null` in the pattern.

## Your task
Help the team. Do whatever you find necessary. 

You have been invited to a slack channel dedicated to the recruitment.

Feel free to ask questions regarding this or any task on slack. 