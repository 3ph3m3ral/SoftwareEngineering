## Distributed caching 

Distributed caching is a technique used to improve the performance of a distributed computing system, 
such as a computer network or cloud system. It consists in the use of a cache, i.e. a fast access working memory, 
shared by several components of the distributed system. When a system component needs to access certain information, 
before going to look for it in the main storage system (such as a hard drive or a database),
it checks if this information is already present in the cache. 

In this way, if the information has already been previously requested by some other component 
of the system and stored in the cache, the component in question can retrieve it directly 
from the cache without having to look for it again in the main storage system, thus obtaining a considerable improvement of performance.

Distributed caching is often used in systems that require a high level of scalability and availability, 
as it allows the cache to be distributed across multiple system components in order to reduce the load on each individual component
and ensure service continuity even in case of breakdowns or malfunctions of one or more components.
