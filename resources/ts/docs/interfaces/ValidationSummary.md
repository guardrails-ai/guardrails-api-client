[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ValidationSummary

# Interface: ValidationSummary

**`Export`**

ValidationSummary

## Table of contents

### Properties

- [errorSpans](ValidationSummary.md#errorspans)
- [failureReason](ValidationSummary.md#failurereason)
- [propertyPath](ValidationSummary.md#propertypath)
- [validatorName](ValidationSummary.md#validatorname)
- [validatorStatus](ValidationSummary.md#validatorstatus)

## Properties

### errorSpans

• `Optional` **errorSpans**: [`ErrorSpan`](ErrorSpan.md)[]

**`Memberof`**

ValidationSummary

#### Defined in

src/models/ValidationSummary.ts:53

___

### failureReason

• `Optional` **failureReason**: `string`

The error message indicating why validation failed.

**`Memberof`**

ValidationSummary

#### Defined in

src/models/ValidationSummary.ts:47

___

### propertyPath

• `Optional` **propertyPath**: `string`

The JSON path to the property which was validated that produced this log.

**`Memberof`**

ValidationSummary

#### Defined in

src/models/ValidationSummary.ts:41

___

### validatorName

• **validatorName**: `string`

The class name of the validator.

**`Memberof`**

ValidationSummary

#### Defined in

src/models/ValidationSummary.ts:29

___

### validatorStatus

• **validatorStatus**: [`ValidationSummaryValidatorStatusEnum`](../modules.md#validationsummaryvalidatorstatusenum)

**`Memberof`**

ValidationSummary

#### Defined in

src/models/ValidationSummary.ts:35
