# Week 2 — Distributed Tracing

The third week of the AWS Cloud Project Bootcamp focused on Distributed Tracing & Observability, which was a bit more challenging but equally important. We learned about instrumenting our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider. We also Instrument AWS X-Ray into backend flask application. This includes configuration and provision of X-Ray daemon within docker-compose and sending data back to X-Ray API. The guest instructor from Honeycomb.io, Jessica Joy Kerr, provided us with real-world examples and helped us understand how to apply these concepts in our own projects.

The main objectives & tasks of week 2 includes: 
- Instrument the backend flask application to use Open Telemetry (OTEL) with Honeycomb.io and run queries to explore traces.
- Instrument AWS X-Ray into backend flask application & Configure provision X-Ray daemon within docker-compose. 
- Integrate Rollbar for Error Logging & trigger and observe an error. 
- Install WatchTower and write a custom logger to send application log data to CloudWatch Log group

# Week 2 — Homework and Challenges

 After watching the videos, including the live webinar i attended, I have completed the tasks as follow:
 - Instrument Honeycomb with OTEL - understanding the overall process was a bit complex but thanks to Andrew and Jessica it was a matter of taking your time and following the instructions. I was able to instrument using Honeycomb as shown bellow:
 -![image](https://user-images.githubusercontent.com/77783631/230789628-7074c1aa-45ef-47c9-b5bf-61310ae3930e.png)


- Instrument AWS X-Ray – this task allows me to explore X-Ray  I was ably to instrument using X-Ray. The subsegment part of the task was a bit challenging but after some challenges i was ably to finish the tasks. The following images shows the log and traces on X-RAY:
-
 <img width="692" alt="db" src="https://user-images.githubusercontent.com/77783631/230789953-bdaf1b47-e546-44d2-b375-83535dec9821.png">
 <img width="692" alt="db" src="https://user-images.githubusercontent.com/77783631/230789965-bb1922a0-ae6e-48f4-a120-bd9e3165d22c.png">
 
 
 - Finally i have implemented Rollbar and cloudwatch logs for error logging. 
 
 <img width="692" alt="db" src="https://user-images.githubusercontent.com/77783631/230789980-e337f3fd-b628-4f5d-a879-bf1eed7b9e17.png">
 
 <img width="692" alt="db" src="https://user-images.githubusercontent.com/77783631/230789988-012f9a5b-5d4c-4dc0-ad3b-85252efd4a6e.png">

## Final Tought on First week.
This week was a bit challenging interms on understanding the process of instrumentation. It's great to learn about logging and instrumentation that will help me to manage the cloud infrustructure. 
