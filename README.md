# 1kkInsertPyhonSQL

#FAÇA ESSES INSERTS PARA O SCRIPT FUNCIONAR
USE laravel;

INSERT INTO `subscription_plans` (`id`, `name`, `storage_limit`, `price`, `description`, `created_at`, `updated_at`) VALUES
(1, 'Plano Básico', 10, 9.99, 'Plano inicial com 10GB de armazenamento', NOW(), NOW()),
(2, 'Plano Pro', 100, 29.99, 'Plano profissional com 100GB de armazenamento', NOW(), NOW()),
(3, 'Plano Premium', 1000, 59.99, 'Plano premium com 1TB e suporte prioritário', NOW(), NOW());
