## CI firmware compilation

The [ESPHome compatibility workflow](../.github/workflows/esphome-build.yml) builds
the Smartmi Evaporative Humidifier 2 and Mi Air Purifier 3C examples on
ESPHome 2026.9.1 and 2026.10.0. The workflow runs on component/config changes,
PRs, and manual dispatch.

The checked-out repository's `components/` directory is used as the local
`external_components` source. Example YAML files remain unchanged.
Synthetic values for `!secret` entries are generated in the temporary
`.ci/` directory; they are **not** suitable for real devices.

To reproduce one build after installing ESPHome:

```sh
python .github/scripts/prepare_ci_example.py \
  --source config/zhimi.humidifier.ca4.yaml \
  --target .ci/zhimi.humidifier.ca4.yaml

esphome config .ci/zhimi.humidifier.ca4.yaml
esphome compile .ci/zhimi.humidifier.ca4.yaml
```

Each job compiles real firmware, not just validates YAML. The job matrix is
intentionally small to keep routine PR costs bounded. It cannot replace
device-specific hardware and UART regression testing.
