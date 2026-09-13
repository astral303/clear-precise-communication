$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
uv run python install/install.py @args
