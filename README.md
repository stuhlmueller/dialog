To run locally, set up [Logistician](https://github.com/stuhlmueller/logistician), then run:

```
logistician run experiments/babi-1-a/ -o "--optimize"
```

To analyze `trace.json` files generated from cloud runs, use [jq](https://stedolan.github.io/jq/). For example:

```
jq -c '[input_filename, .[-1].devStats.responses]' data/*/results/trace.json
```