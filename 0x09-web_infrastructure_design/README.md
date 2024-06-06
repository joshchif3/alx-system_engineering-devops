
![0-simple_web_stack](https://github.com/joshchif3/alx-system_engineering-devops/assets/122808743/f2032856-57b8-434d-8942-e2bca9893671)


![1-distributed_web_infrastructure](https://github.com/joshchif3/alx-system_engineering-devops/assets/122808743/eb4ed693-ad30-4d62-9021-e72b6af1e637)



![3-scale_up](https://github.com/joshchif3/alx-system_engineering-devops/assets/122808743/c88bf60c-21cc-4e2f-8bea-b3e92520b284)









0. Simple Web Stack
Description
This is a simple web infrastructure that hosts the website www.foobar.com on a single server setup. It includes basic components required to serve a web application.

Infrastructure Components
1 Server
1 Web Server (Nginx)
1 Application Server
1 Database (MySQL)
1 Set of Application Files (Code Base)
Specifics About This Infrastructure
Web Server (Nginx):

The web server handles HTTP requests, serves static content, and acts as a reverse proxy to pass requests to the application server.
Application Server:

The application server processes dynamic content and executes the application code.
Database (MySQL):

The database server stores and manages data for the application. It handles all read and write operations required by the application.
Issues With This Infrastructure
Single Point of Failure (SPOF):

The entire application runs on a single server. If this server goes down, the entire website becomes unavailable.
Scalability:

This setup cannot handle high traffic efficiently. All requests are processed by a single server, leading to performance bottlenecks as traffic increases.
Security:

Without proper security measures like firewalls and SSL certificates, the application is vulnerable to attacks. Data transmitted over the network is not encrypted, exposing it to potential interception.
No Redundancy:

There is no redundancy in this setup. If any component fails (web server, application server, or database), the entire service is impacted.
No Monitoring:

Without monitoring tools, it is difficult to track the performance and health of the server, making it challenging to detect and address issues proactively.

1. Distributed web infrastructure

Description
This is a distributed web infrastructure that attempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica).

Specifics About This Infrastructure
The distribution algorithm the load balancer is configured with and how it works:

The HAProxy load balancer is configured with the Round Robin distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.
The setup enabled by the load-balancer:

The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, the load balancer distributes workloads across all nodes in order to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an Active-Passive setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.
How a database Primary-Replica (Master-Slave) cluster works:

A Primary-Replica setup configures one server to act as the Primary server and the other server to act as a Replica of the Primary server. However, the Primary server is capable of performing read/write requests whilst the Replica server is only capable of performing read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.
The difference between the Primary node and the Replica node in regard to the application:

The Primary node is responsible for all the write operations the site needs whilst the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.
Issues With This Infrastructure
There are multiple SPOF (Single Point Of Failure):

For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.
Security issues:

The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.
No monitoring:

We have no way of knowing the status of each server since they're not being monitored.


2. Secured and Monitored Web Infrastructure
Description
This is a secured and monitored web infrastructure that ensures encrypted traffic and system monitoring. It improves upon the previous infrastructure by addressing security and monitoring concerns.

Specifics About This Infrastructure
Additional Elements and Reasons:

3 Firewalls: Protect the network by filtering incoming and outgoing traffic based on predetermined security rules.
1 SSL Certificate: Encrypts the traffic between the web server and clients to prevent eavesdropping.
3 Monitoring Clients: Collect data for Sumologic or other monitoring services to track server performance and detect issues.
Firewalls:

Firewalls are used to block unauthorized access while permitting outward communication. They add a layer of security by controlling the incoming and outgoing network traffic based on security rules.
Traffic served over HTTPS:

Serving traffic over HTTPS ensures that the data transmitted between the client and server is encrypted, protecting against interception and tampering.
Monitoring:

Monitoring is used to track the health and performance of the servers. The monitoring tool collects data on various metrics such as CPU usage, memory usage, disk activity, and network traffic.
Monitoring Tool Data Collection:

The monitoring tool collects data through agents installed on the servers, which send performance metrics and logs to a centralized monitoring system.
Monitoring Web Server QPS (Queries Per Second):

To monitor web server QPS, you can configure the monitoring tool to track the number of queries or requests per second the server is handling. This helps in understanding the load and performance of the server.
Issues With This Infrastructure
Terminating SSL at the Load Balancer Level:

Terminating SSL at the load balancer means that the traffic between the load balancer and the backend servers is not encrypted, which could be a security risk if the internal network is compromised.
Only One MySQL Server Capable of Accepting Writes:

Having only one MySQL server capable of accepting writes is an issue because it creates a single point of failure. If the primary MySQL server goes down, no write operations can be performed, impacting the functionality of the application.
Servers with All the Same Components:

Having servers with all the same components (database, web server, and application server) might be a problem because it does not allow for scaling specific components independently. It can also lead to resource contention and makes maintenance more complex.
