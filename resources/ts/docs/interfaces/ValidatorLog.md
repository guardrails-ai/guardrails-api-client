[@guardrails-ai/api-client](../README.md) / [Exports](../modules.md) / ValidatorLog

# Interface: ValidatorLog

**`Export`**

ValidatorLog

## Table of contents

### Properties

- [endTime](ValidatorLog.md#endtime)
- [instanceId](ValidatorLog.md#instanceid)
- [propertyPath](ValidatorLog.md#propertypath)
- [registeredName](ValidatorLog.md#registeredname)
- [startTime](ValidatorLog.md#starttime)
- [validationResult](ValidatorLog.md#validationresult)
- [validatorName](ValidatorLog.md#validatorname)
- [valueAfterValidation](ValidatorLog.md#valueaftervalidation)
- [valueBeforeValidation](ValidatorLog.md#valuebeforevalidation)

## Properties

### endTime

• `Optional` **endTime**: `Date`

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:80

___

### instanceId

• `Optional` **instanceId**: `string` \| `number`

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:44

___

### propertyPath

• **propertyPath**: `string`

The JSON path to the property which was validated that produced this log.

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:50

___

### registeredName

• **registeredName**: `string`

The registry id of the validator.

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:38

___

### startTime

• `Optional` **startTime**: `Date`

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:74

___

### validationResult

• `Optional` **validationResult**: [`ValidatorLogValidationResult`](ValidatorLogValidationResult.md)

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:68

___

### validatorName

• **validatorName**: `string`

The class name of the validator.

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:32

___

### valueAfterValidation

• `Optional` **valueAfterValidation**: `any`

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:62

___

### valueBeforeValidation

• **valueBeforeValidation**: `any`

**`Memberof`**

ValidatorLog

#### Defined in

src/models/ValidatorLog.ts:56
