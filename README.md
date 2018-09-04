## AlexF's Elastic{ON} Tour 2018 Demo Repo

This is not production ready and includes a pre-production version of Kibana. There is a good chance that things will break, it is only meant to be a demo environment.

**Not all images and assets were created by Elastic, please to do not redistribute**

The builds found in this repo have an early version of Spaces. There is also an up to date build of Canvas from master. I am hoping to add a few more future features to this build as well. There is a good chance I'll upload a snapshot of data / dashboards as well so it's easier to get started.

Follow the instructions below to install locally

1. [Download](https://drive.google.com/open?id=1puNqeAPjNt4AfG-oscW8eRo9tNS42rGu) and unzip `elasticsearch-7.0.0-alpha1-SNAPSHOT.zip`, navigate to the directory and run `bin/elasticsearch`
2. Choose from `kibana-7.0.0-alpha1-SNAPSHOT-darwin-x86_64.zip`, `kibana-7.0.0-alpha1-SNAPSHOT-linux-x86_64.zip` and `kibana-7.0.0-alpha1-SNAPSHOT-windows-x86_64.zip` depending on your OS. [Download](https://drive.google.com/open?id=1i0hsiWTVkxkDq8xT9EDmEX0LFO6-yn5X) and unzip
3. From the `kibana` directory, [download](https://drive.google.com/open?id=18W_ypEpATl2RqKET1OWqnD0YgALcaGmT) and install Canvas as a plugin.
   * `NODE_OPTIONS="--max-old-space-size=4096" ./bin/kibana-plugin install \
      file:///[PATH TO FILE]/canvas.zip`
4. When the installation is complete, from the directory run `bin/kibana`.
5. Spin up Kibana from it's default host `localhost:5601`. Download the license file [here](https://drive.google.com/open?id=1Q7ru9TbxcTdLuAX4XyT_UeKIH8DaSVNq). Upload this license in the License Management UI.
6. Kill Kibana
7. With Elasticsearch running, open a new terminal window and navigate to the `elasticsearch-7.0.0-alpha1-SNAPSHOT` directory. Run `bin/elasticsearch-setup-passwords interactive` and changes all passwords to `Elastic2018!`
8. When complete, kill Elasticsearch. Download the `elasticsearch.yml` and `kibana.yml` files from [here](https://drive.google.com/open?id=1s7LKwKuZpnPkJyKIYkO4jATzDBYgjE0J). Replace them in their appropriate directories.
    * I have these running on `localhost:9400` and `localhost:5610` so I can still run other dev builds locally. Feel free to change in the settings but all scripts are setup for these endpoints.
10. Start Elasticsearch and Kibana, add both the flights and web logs sample data to the cluster
11. In the [scripts directory](https://github.com/alexfrancoeur/elasticon_tour_2018_alexf/tree/master/all_scripts) of this repo, start running the `canvas_intro_stats.py` script to start generating content for the workpad
12. Create an index pattern for `canvas_stats`
13. From the [canvas_workpads directory](https://github.com/alexfrancoeur/elasticon_tour_2018_alexf/tree/master/all_canvas_workpads), download the `Elastic{ON} Tour 2018 Kibana Canvas.json` workpad. Drag and drop it into the Canvas workpad table. You should have a demoable workpad ready to go.
14. Demo script is available [here](https://docs.google.com/document/d/1k3kjuscjdLkW_ECTMT9qE9Ck8Rdcl6IELiZO78aboWs/edit?usp=sharing) if needed
