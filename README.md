# Backlog Analyzer

Grab GitHub issues from a repository and answer questions about them with an LLM.

The chatbot will summarize top 20 open issues by cosine similarity on embeddings.

## Installation

``` shell
uv tool install .
```

## Usage

Requires OPENAI_API_KEY environment variable to be set.

```shell
$ banal -r pulumi/pulumi-azuread -q "What are the issues with outputs?"                                               ~

The issues related to outputs in the provided GitHub issues involve several aspects:

1. **Deprecation Warning in Outputs (pulumi/pulumi-azuread#267)**:
   - The function `GetServicePrincipal` generates a deprecation warning related to output properties (`features`) that cannot be controlled or modified, which becomes annoying when the function is called multiple times.

2. **State File Desynchronization (pulumi/pulumi-azuread#1169)**:
   - When updating certain properties of an application (e.g., owners), the API permissions are lost from the actual Azure resource but still exist in the Pulumi state file. This results in a discrepancy between the actual state in Azure and what Pulumi believes to be the state, requiring a manual refresh to correct.

3. **Identifier URI Loss on Update (pulumi/pulumi-azuread#1036)**:
   - If any property of an existing Azure AD application is updated, the Identifier URI set via `ApplicationIdentifierUri` might be removed in Azure, even though it remains in the Pulumi stack, causing a disconnect between the actual Azure state and the expected Pulumi state.

These issues indicate challenges related to maintaining consistency between Pulumi-managed resources and the actual state of resources in Azure, especially when outputs are involved.
```
