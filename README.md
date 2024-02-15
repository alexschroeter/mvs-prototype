# Multiview-Stitcher Prototype

This is a prototype for a project. To test functionality, hardware, and test integration.

It consists of two repositories:
 - https://github.com/alexschroeter/mvs-prototype/
 - https://github.com/alexschroeter/mvs-prototype-privat/

## Permissions

The Personal Access Token that triggers the event needs `contents write`[link](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#create-a-repository-dispatch-event) permissions for the repository.

If this permission is as vulnerable as having the self-hosted runner connected to this repository an (also not optimal) alternative might be to run on a timer from the private repository.
