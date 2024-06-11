[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ValidationOutcome

# Interface: ValidationOutcome

The output from a Guard execution.

**`Export`**

ValidationOutcome

## Table of contents

### Properties

- [error](ValidationOutcome.md#error)
- [rawLlmOutput](ValidationOutcome.md#rawllmoutput)
- [reask](ValidationOutcome.md#reask)
- [validatedOutput](ValidationOutcome.md#validatedoutput)
- [validationPassed](ValidationOutcome.md#validationpassed)

## Properties

### error

• `Optional` **error**: `string`

If the validation process raised a handleable exception, this field will contain the error message.

**`Memberof`**

ValidationOutcome

#### Defined in

src/models/ValidationOutcome.ts:57

___

### rawLlmOutput

• `Optional` **rawLlmOutput**: `string`

The raw, unchanged string content from the LLM call.

**`Memberof`**

ValidationOutcome

#### Defined in

src/models/ValidationOutcome.ts:33

___

### reask

• `Optional` **reask**: [`Reask`](Reask.md)

If validation continuously fails and all allocated reasks are used, this field will contain the final reask that would have been sent to the LLM if additional reasks were available.

**`Memberof`**

ValidationOutcome

#### Defined in

src/models/ValidationOutcome.ts:45

___

### validatedOutput

• `Optional` **validatedOutput**: `string` \| `Record`\<`string`, `any`\>

**`Memberof`**

ValidationOutcome

#### Defined in

src/models/ValidationOutcome.ts:39

___

### validationPassed

• `Optional` **validationPassed**: `boolean`

A boolean to indicate whether or not the LLM output passed validation.  If this is False, the validated_output may be invalid.

**`Memberof`**

ValidationOutcome

#### Defined in

src/models/ValidationOutcome.ts:51
