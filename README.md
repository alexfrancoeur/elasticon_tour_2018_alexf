## AlexF's Elastic{ON} Tour 2018 Demo Repo

This is not production ready and includes a pre-production version of Kibana. There is a good chance that things will break, it is only meant to be a demo environment.

The builds found in this repo have an early version of Spaces. There is also an up to date build of Canvas from master. I am hoping to add a few more future features to this build as well. There is a good chance I'll upload a snapshot of data / dashboards as well so it's easier to get started.

Follow the instructions below to install locally

1. [Download](https://drive.google.com/open?id=1puNqeAPjNt4AfG-oscW8eRo9tNS42rGu) and unzip `elasticsearch-7.0.0-alpha1-SNAPSHOT.zip`, navigate to the directory and run `bin/elasticsearch`
2. Choose from `kibana-7.0.0-alpha1-SNAPSHOT-darwin-x86_64.zip`, `kibana-7.0.0-alpha1-SNAPSHOT-linux-x86_64.zip` and `kibana-7.0.0-alpha1-SNAPSHOT-windows-x86_64.zip` depending on your OS. [Download](https://drive.google.com/open?id=1i0hsiWTVkxkDq8xT9EDmEX0LFO6-yn5X) and unzip
3. From the `kibana` directory, [download](https://drive.google.com/open?id=18W_ypEpATl2RqKET1OWqnD0YgALcaGmT) and install Canvas as a plugin.
   * `NODE_OPTIONS="--max-old-space-size=4096" ./bin/kibana-plugin install \
      file:///[PATH TO FILE]/canvas.zip`
4. When the installation is complete, from the directory run `bin/kibana`
5. Feel free to import the [`makelog`](https://www.npmjs.com/package/makelogs) in the `saved_objects` folder. Import any of the workpads in the `canvas_workpads` and run any of the `scripts` to start generating data.
6. In order to take full advantage of all features available, you may want to run the 30 day trial


More Spaces / Canvas workpad specific script and instructions to come...
