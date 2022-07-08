{
    'ModelPackageName': 'string',
    'ModelPackageGroupName': 'string',
    'ModelPackageVersion': 123,
    'ModelPackageArn': 'string',
    'ModelPackageDescription': 'string',
    'CreationTime': datetime(2015, 1, 1),
    'InferenceSpecification': {
        'Containers': [
            {
                'ContainerHostname': 'string',
                'Image': 'string',
                'ImageDigest': 'string',
                'ModelDataUrl': 'string',
                'ProductId': 'string',
                'Environment': {
                    'string': 'string'
                },
                'ModelInput': {
                    'DataInputConfig': 'string'
                },
                'Framework': 'string',
                'FrameworkVersion': 'string',
                'NearestModelName': 'string'
            },
        ],
        'SupportedTransformInstanceTypes': [
            'ml.m4.xlarge' | 'ml.m4.2xlarge' | 'ml.m4.4xlarge' | 'ml.m4.10xlarge' | 'ml.m4.16xlarge' | 'ml.c4.xlarge' | 'ml.c4.2xlarge' | 'ml.c4.4xlarge' | 'ml.c4.8xlarge' | 'ml.p2.xlarge' | 'ml.p2.8xlarge' | 'ml.p2.16xlarge' | 'ml.p3.2xlarge' | 'ml.p3.8xlarge' | 'ml.p3.16xlarge' | 'ml.c5.xlarge' | 'ml.c5.2xlarge' | 'ml.c5.4xlarge' | 'ml.c5.9xlarge' | 'ml.c5.18xlarge' | 'ml.m5.large' | 'ml.m5.xlarge' | 'ml.m5.2xlarge' | 'ml.m5.4xlarge' | 'ml.m5.12xlarge' | 'ml.m5.24xlarge' | 'ml.g4dn.xlarge' | 'ml.g4dn.2xlarge' | 'ml.g4dn.4xlarge' | 'ml.g4dn.8xlarge' | 'ml.g4dn.12xlarge' | 'ml.g4dn.16xlarge',
        ],
        'SupportedRealtimeInferenceInstanceTypes': [
            'ml.t2.medium' | 'ml.t2.large' | 'ml.t2.xlarge' | 'ml.t2.2xlarge' | 'ml.m4.xlarge' | 'ml.m4.2xlarge' | 'ml.m4.4xlarge' | 'ml.m4.10xlarge' | 'ml.m4.16xlarge' | 'ml.m5.large' | 'ml.m5.xlarge' | 'ml.m5.2xlarge' | 'ml.m5.4xlarge' | 'ml.m5.12xlarge' | 'ml.m5.24xlarge' | 'ml.m5d.large' | 'ml.m5d.xlarge' | 'ml.m5d.2xlarge' | 'ml.m5d.4xlarge' | 'ml.m5d.12xlarge' | 'ml.m5d.24xlarge' | 'ml.c4.large' | 'ml.c4.xlarge' | 'ml.c4.2xlarge' | 'ml.c4.4xlarge' | 'ml.c4.8xlarge' | 'ml.p2.xlarge' | 'ml.p2.8xlarge' | 'ml.p2.16xlarge' | 'ml.p3.2xlarge' | 'ml.p3.8xlarge' | 'ml.p3.16xlarge' | 'ml.c5.large' | 'ml.c5.xlarge' | 'ml.c5.2xlarge' | 'ml.c5.4xlarge' | 'ml.c5.9xlarge' | 'ml.c5.18xlarge' | 'ml.c5d.large' | 'ml.c5d.xlarge' | 'ml.c5d.2xlarge' | 'ml.c5d.4xlarge' | 'ml.c5d.9xlarge' | 'ml.c5d.18xlarge' | 'ml.g4dn.xlarge' | 'ml.g4dn.2xlarge' | 'ml.g4dn.4xlarge' | 'ml.g4dn.8xlarge' | 'ml.g4dn.12xlarge' | 'ml.g4dn.16xlarge' | 'ml.r5.large' | 'ml.r5.xlarge' | 'ml.r5.2xlarge' | 'ml.r5.4xlarge' | 'ml.r5.12xlarge' | 'ml.r5.24xlarge' | 'ml.r5d.large' | 'ml.r5d.xlarge' | 'ml.r5d.2xlarge' | 'ml.r5d.4xlarge' | 'ml.r5d.12xlarge' | 'ml.r5d.24xlarge' | 'ml.inf1.xlarge' | 'ml.inf1.2xlarge' | 'ml.inf1.6xlarge' | 'ml.inf1.24xlarge',
        ],
        'SupportedContentTypes': [
            'string',
        ],
        'SupportedResponseMIMETypes': [
            'string',
        ]
    },
    'SourceAlgorithmSpecification': {
        'SourceAlgorithms': [
            {
                'ModelDataUrl': 'string',
                'AlgorithmName': 'string'
            },
        ]
    },
    'ValidationSpecification': {
        'ValidationRole': 'string',
        'ValidationProfiles': [
            {
                'ProfileName': 'string',
                'TransformJobDefinition': {
                    'MaxConcurrentTransforms': 123,
                    'MaxPayloadInMB': 123,
                    'BatchStrategy': 'MultiRecord' | 'SingleRecord',
                    'Environment': {
                        'string': 'string'
                    },
                    'TransformInput': {
                        'DataSource': {
                            'S3DataSource': {
                                'S3DataType': 'ManifestFile' | 'S3Prefix' | 'AugmentedManifestFile',
                                'S3Uri': 'string'
                            }
                        },
                        'ContentType': 'string',
                        'CompressionType': 'None' | 'Gzip',
                        'SplitType': 'None' | 'Line' | 'RecordIO' | 'TFRecord'
                    },
                    'TransformOutput': {
                        'S3OutputPath': 'string',
                        'Accept': 'string',
                        'AssembleWith': 'None' | 'Line',
                        'KmsKeyId': 'string'
                    },
                    'TransformResources': {
                        'InstanceType': 'ml.m4.xlarge' | 'ml.m4.2xlarge' | 'ml.m4.4xlarge' | 'ml.m4.10xlarge' | 'ml.m4.16xlarge' | 'ml.c4.xlarge' | 'ml.c4.2xlarge' | 'ml.c4.4xlarge' | 'ml.c4.8xlarge' | 'ml.p2.xlarge' | 'ml.p2.8xlarge' | 'ml.p2.16xlarge' | 'ml.p3.2xlarge' | 'ml.p3.8xlarge' | 'ml.p3.16xlarge' | 'ml.c5.xlarge' | 'ml.c5.2xlarge' | 'ml.c5.4xlarge' | 'ml.c5.9xlarge' | 'ml.c5.18xlarge' | 'ml.m5.large' | 'ml.m5.xlarge' | 'ml.m5.2xlarge' | 'ml.m5.4xlarge' | 'ml.m5.12xlarge' | 'ml.m5.24xlarge' | 'ml.g4dn.xlarge' | 'ml.g4dn.2xlarge' | 'ml.g4dn.4xlarge' | 'ml.g4dn.8xlarge' | 'ml.g4dn.12xlarge' | 'ml.g4dn.16xlarge',
                        'InstanceCount': 123,
                        'VolumeKmsKeyId': 'string'
                    }
                }
            },
        ]
    },
    'CertifyForMarketplace': True | False,
    'ModelApprovalStatus': 'Approved' | 'Rejected' | 'PendingManualApproval',
    'ModelPackageStatus': 'Pending' | 'InProgress' | 'Completed' | 'Failed' | 'Deleting',
    'ModelPackageStatusDetails': {
        'ValidationStatuses': [
            {
                'Name': 'string',
                'Status': 'NotStarted' | 'InProgress' | 'Completed' | 'Failed',
                'FailureReason': 'string'
            },
        ],
        'ImageScanStatuses': [
            {
                'Name': 'string',
                'Status': 'NotStarted' | 'InProgress' | 'Completed' | 'Failed',
                'FailureReason': 'string'
            },
        ]
    },


    'CreatedBy': {
        'UserProfileArn': 'string',
        'UserProfileName': 'string',
        'DomainId': 'string'
    },
    'MetadataProperties': {
        'CommitId': 'string',
        'Repository': 'string',
        'GeneratedBy': 'string',
        'ProjectId': 'string'
    },
    'ModelMetrics': {
        'ModelQuality': {
            'Statistics': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'Constraints': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        },
        'ModelDataQuality': {
            'Statistics': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'Constraints': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        },
        'Bias': {
            'Report': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'PreTrainingReport': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'PostTrainingReport': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        },
        'Explainability': {
            'Report': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        }
    },
    'LastModifiedTime': datetime(2015, 1, 1),
    'LastModifiedBy': {
        'UserProfileArn': 'string',
        'UserProfileName': 'string',
        'DomainId': 'string'
    },
    'ApprovalDescription': 'string',
    'CustomerMetadataProperties': {
        'string': 'string'
    },
    'DriftCheckBaselines': {
        'Bias': {
            'ConfigFile': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'PreTrainingConstraints': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'PostTrainingConstraints': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        },
        'Explainability': {
            'Constraints': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'ConfigFile': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        },
        'ModelQuality': {
            'Statistics': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'Constraints': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        },
        'ModelDataQuality': {
            'Statistics': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            },
            'Constraints': {
                'ContentType': 'string',
                'ContentDigest': 'string',
                'S3Uri': 'string'
            }
        }
    },
    'Domain': 'string',
    'Task': 'string',
    'SamplePayloadUrl': 'string',
    'AdditionalInferenceSpecifications': [
        {
            'Name': 'string',
            'Description': 'string',
            'Containers': [
                {
                    'ContainerHostname': 'string',
                    'Image': 'string',
                    'ImageDigest': 'string',
                    'ModelDataUrl': 'string',
                    'ProductId': 'string',
                    'Environment': {
                        'string': 'string'
                    },
                    'ModelInput': {
                        'DataInputConfig': 'string'
                    },
                    'Framework': 'string',
                    'FrameworkVersion': 'string',
                    'NearestModelName': 'string'
                },
            ],
            'SupportedTransformInstanceTypes': [
                'ml.m4.xlarge' | 'ml.m4.2xlarge' | 'ml.m4.4xlarge' | 'ml.m4.10xlarge' | 'ml.m4.16xlarge' | 'ml.c4.xlarge' | 'ml.c4.2xlarge' | 'ml.c4.4xlarge' | 'ml.c4.8xlarge' | 'ml.p2.xlarge' | 'ml.p2.8xlarge' | 'ml.p2.16xlarge' | 'ml.p3.2xlarge' | 'ml.p3.8xlarge' | 'ml.p3.16xlarge' | 'ml.c5.xlarge' | 'ml.c5.2xlarge' | 'ml.c5.4xlarge' | 'ml.c5.9xlarge' | 'ml.c5.18xlarge' | 'ml.m5.large' | 'ml.m5.xlarge' | 'ml.m5.2xlarge' | 'ml.m5.4xlarge' | 'ml.m5.12xlarge' | 'ml.m5.24xlarge' | 'ml.g4dn.xlarge' | 'ml.g4dn.2xlarge' | 'ml.g4dn.4xlarge' | 'ml.g4dn.8xlarge' | 'ml.g4dn.12xlarge' | 'ml.g4dn.16xlarge',
            ],
            'SupportedRealtimeInferenceInstanceTypes': [
                'ml.t2.medium' | 'ml.t2.large' | 'ml.t2.xlarge' | 'ml.t2.2xlarge' | 'ml.m4.xlarge' | 'ml.m4.2xlarge' | 'ml.m4.4xlarge' | 'ml.m4.10xlarge' | 'ml.m4.16xlarge' | 'ml.m5.large' | 'ml.m5.xlarge' | 'ml.m5.2xlarge' | 'ml.m5.4xlarge' | 'ml.m5.12xlarge' | 'ml.m5.24xlarge' | 'ml.m5d.large' | 'ml.m5d.xlarge' | 'ml.m5d.2xlarge' | 'ml.m5d.4xlarge' | 'ml.m5d.12xlarge' | 'ml.m5d.24xlarge' | 'ml.c4.large' | 'ml.c4.xlarge' | 'ml.c4.2xlarge' | 'ml.c4.4xlarge' | 'ml.c4.8xlarge' | 'ml.p2.xlarge' | 'ml.p2.8xlarge' | 'ml.p2.16xlarge' | 'ml.p3.2xlarge' | 'ml.p3.8xlarge' | 'ml.p3.16xlarge' | 'ml.c5.large' | 'ml.c5.xlarge' | 'ml.c5.2xlarge' | 'ml.c5.4xlarge' | 'ml.c5.9xlarge' | 'ml.c5.18xlarge' | 'ml.c5d.large' | 'ml.c5d.xlarge' | 'ml.c5d.2xlarge' | 'ml.c5d.4xlarge' | 'ml.c5d.9xlarge' | 'ml.c5d.18xlarge' | 'ml.g4dn.xlarge' | 'ml.g4dn.2xlarge' | 'ml.g4dn.4xlarge' | 'ml.g4dn.8xlarge' | 'ml.g4dn.12xlarge' | 'ml.g4dn.16xlarge' | 'ml.r5.large' | 'ml.r5.xlarge' | 'ml.r5.2xlarge' | 'ml.r5.4xlarge' | 'ml.r5.12xlarge' | 'ml.r5.24xlarge' | 'ml.r5d.large' | 'ml.r5d.xlarge' | 'ml.r5d.2xlarge' | 'ml.r5d.4xlarge' | 'ml.r5d.12xlarge' | 'ml.r5d.24xlarge' | 'ml.inf1.xlarge' | 'ml.inf1.2xlarge' | 'ml.inf1.6xlarge' | 'ml.inf1.24xlarge',
            ],
            'SupportedContentTypes': [
                'string',
            ],
            'SupportedResponseMIMETypes': [
                'string',
            ]
        },
    ]
}
