SwiftParallelizer
=================

A way to upload large objects in parallel by splitting into small chunks to Openstack swift using Openstack Marconi as the queue transport service.

Usage
=======

<li>
<ul> Install Openstack Swift SAIO</ul></li>
<li><ul> Install Openstack Marconi with MongoDB controller (In-memory). This can be done by modifying dbpath to a tmpfs file system in linux</ul></li>
<li><ul> Put files inside the objects directory </ul></li>
<li><ul> run ./parallelize.sh "filename" "split size" "threadcount"</ul></li>
<li><ul>Example : ./parallelize.sh rollercoaster.jpg 100k 10</ul></li>

