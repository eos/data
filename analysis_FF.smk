from snakemake.utils import min_version
min_version("7")

analysis_file = "analysis_FF.yaml"

rule all:
    input:
        f"{analysis_file}",
        expand([f"steps/{s}" for s in shell(f"eos-analysis list-steps -f {analysis_file}", iterable=True)])
    output:
        touch("steps/all")

STEPS=[s for s in shell(f"eos-analysis list-steps -f {analysis_file}", iterable=True)]
for s in STEPS:
    rule:
        name: f"{s}"
        params:
            step=s,
        input:
            f"{analysis_file}",
            expand([f"steps/{d}" for d in shell(f"eos-analysis list-step-dependencies -f {analysis_file} {s}", iterable=True)])
        output:
            f"steps/{s}"
        shell:
            f"eos-analysis run -f {analysis_file} {{params.step}} > {{output[0]}} 2> /dev/null"
