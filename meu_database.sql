-- ===========================================================
--  POPULANDO ALUNOS (Student = AbstractUser)
-- ===========================================================

INSERT INTO registrations_student
(username, password, email, first_name, last_name, is_staff, is_active, is_superuser)
VALUES
('ana.silva',      'pbkdf2_sha256$fakehash', 'ana@example.com',      'Ana',      'Silva',      0, 1, 0),
('joao.souza',     'pbkdf2_sha256$fakehash', 'joao@example.com',     'João',     'Souza',     0, 1, 0),
('maria.pereira',  'pbkdf2_sha256$fakehash', 'maria@example.com',    'Maria',    'Pereira',   0, 1, 0),
('pedro.almeida',  'pbkdf2_sha256$fakehash', 'pedro@example.com',    'Pedro',    'Almeida',   0, 1, 0),
('lucas.martins',  'pbkdf2_sha256$fakehash', 'lucas@example.com',    'Lucas',    'Martins',   0, 1, 0);

-- Observação:
-- A senha acima é simbólica; para senhas reais deve-se usar createsuperuser
-- ou gerar hash via Django.


-- ===========================================================
--  POPULANDO CURSOS
-- ===========================================================

INSERT INTO registrations_course (title, description)
VALUES
('Python para Iniciantes', 'Curso introdutório cobrindo lógica, variáveis, loops e funções.'),
('Django Web Framework', 'Construção de aplicações web com Django, ORM, templates e deploy.'),
('Banco de Dados SQL', 'Fundamentos de SQL, joins, normalização e modelagem.'),
('Git e GitHub', 'Versionamento, branches, pull requests e boas práticas.'),
('Machine Learning Básico', 'Introdução a modelos supervisionados, regressão e classificação.');


-- ===========================================================
--  RELACIONAMENTO MANY-TO-MANY (COURSE ↔ STUDENT)
--  Tabela: registrations_course_students
-- ===========================================================

-- Estrutura típica:
-- registrations_course_students (id, course_id, student_id)

INSERT INTO registrations_course_students (course_id, student_id)
VALUES
(1, 1),
(1, 2),
(1, 3),

(2, 2),
(2, 3),
(2, 4),

(3, 1),
(3, 4),
(3, 5),

(4, 5),

(5, 1),
(5, 2),
(5, 5);
